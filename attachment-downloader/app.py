import imaplib
import email
import os

USEREMAIL = "example@mail.com"
USERPASS = "Example000"


def downloadAttachment():

    mail = imaplib.IMAP4_SSL("imap.gmail.com", port=993)
    mail.login(USEREMAIL, USERPASS)

    mail.select()

    result, data = mail.uid("search", None, "ALL")
    mails = len(data[0].split())

    for i in range(mails):
        latestEmailUID = data[0].split()[i]
        result, emailData = mail.uid("fetch", latestEmailUID, "(RFC822)")

        rawEmail = emailData[0][1]
        rawEmailString = rawEmail.decode("utf-8")
        emailMessage = email.message_from_string(rawEmailString)

        for content in emailMessage.walk():
            if content.get_content_maintype() == "multipart":
                continue
            if content.get("Content-Disposition") is None:
                continue
            fileName = content.get_filename()
            fromEmail = emailMessage["from"]

            if bool(fileName):
                if fileName.endswith(".pdf"):
                    if fileName.startswith("SOMETHING"):
                        cwd = os.getcwd()
                        filePath = os.path.join("PATH", fileName)
                        if not os.path.isfile(filePath):
                            fileWrite = open(filePath, "wb")
                            fileWrite.write(content.get_payload(decode=True))
                            fileWrite.close()
                        uid = latestEmailUID.decode("utf-8")
                        print(
                            f'Downloaded "{fileName}" in "{cwd}\\download" from "{fromEmail}" with UID "{uid}"'
                        )


downloadAttachment()
