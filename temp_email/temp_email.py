from typing import Optional
import requests
import time
import uuid


class Maildrop(object):
    _apikey = "QM8VTHrLR2JloKTJMZ3N6Qa93FVsx8LapKCzEjui"
    _inbox = "https://api.maildrop.cc/v2/mailbox"
    _search_fields = ("sender", "subject", "body",)

    def __init__(
        self,
        address: Optional[str] = None,
        message_filter: Optional[str] = None
    ) -> None:
        """Create an instance of the Maildrop.cc client.

            :param address: Optional address to monitor on maildrop.
                Can be a full email with or without domain.
                Defaults to a random uuid.
                Note the address if you plan to re-use it in the future.
            :param message_filter: Optional text to search for in
                sender, subject, and body fields.
        """
        if address and "@" in address:
            # drop the domain from the email address
            self._address = address.rsplit("@", 1)[0]
        elif address:
            # specifying a specific maildrop.cc email for easy re-use
            self._address = address
        else:
            # generate a completely random (throwaway) maildrop address
            self._address = uuid.uuid4().hex

        self._filter = message_filter
        self._seen = set()
        self._emails = list()
        self._client = requests.Session()
        self._client.headers.update({
            "Content-Type": "application/json",
            "x-api-key": self._apikey
        })
        print(f"maildrop address set to {self._address}@maildrop.cc")

    @property
    def address(self) -> str:
        """Returns the temporary email address being monitored."""
        return f"{self._address}@maildrop.cc"

    @property
    def emails(self) -> list:
        """Returns a list of the emails collected during the monitor loop."""
        return self._emails

    def _get_body(self, email_id: str) -> str:
        """Retrieves the body of an email.

            :param email_id: The unique identifier of the email to retrieve.
            :returns: The body of the requested email.
            :rtype: str
        """
        resp = self._client.get(f"{self._inbox}/{self._address}/{email_id}")
        if not resp.ok:
            raise RuntimeError(
                f"Issue retrieving specific email ({email_id}) from inbox."
            )
        return resp.json().get("body", "")

    def get_emails(self) -> list:
        """Retrieves all unseen emails."""
        resp = self._client.get(f"{self._inbox}/{self._address}")
        if not resp.ok:
            raise RuntimeError("Issue retrieving inbox from maildrop.cc.")
        new_emails = []
        for email in resp.json().get("messages", []):
            email_id = email.get("id")
            if email_id in self._seen:
                continue
            # keep reference of all seen emails to prevent returning duplicates
            self._seen.add(email_id)
            email["body"] = self._get_body(email_id)
            if self._filter:
                if any([
                    self._filter in email.get(field, "")
                    for field in self._search_fields
                ]):
                    new_emails.append(email)
            else:
                new_emails.append(email)
        self._emails.extend(new_emails)
        return new_emails

    def monitor_inbox(self, interval: int = 5) -> None:
        """Check for unseen emails at an interval until told to stop.

            :param interval: Optional number of seconds to wait
                before re-checking for unseen emails.
                Defaults to 5 seconds.
        """
        print(f"checking inbox every {interval} seconds")
        print("to stop monitoring loop, press & hold ctrl+c")
        while True:
            try:
                emails = self.get_emails()
                if emails:
                    print(f"found {len(emails)} new emails")
                    for email in emails:
                        print("email_id:", email.get("id"))
                        print("from:", email.get("sender"))
                        print("subject:", email.get("subject"))
                        print("body:", email.get("body"))
                        print("\n\n===\n\n")
                time.sleep(interval)
            except KeyboardInterrupt:
                print("stopping inbox monitor")
                break


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        "--address",
        help=(
            "A specific maildrop.cc email address to monitor. "
            "If omitted, a randomly-generated UUID4 is used."
        ),
        default=None
    )
    parser.add_argument(
        "-f",
        "--filter",
        help=(
            "A string to search for in new emails. "
            "If omitted, all new emails are returned."
        ),
        default=None
    )
    args = parser.parse_args()
    md = Maildrop(address=args.address, message_filter=args.filter)
    md.monitor_inbox()
