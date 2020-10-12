import click
import locale
import requests


# # # # # # # # # # # # # # # # # Constants # # # # # # # # # # # # # # # # # #
URL = 'https://wttr.in/{loc}?{fore}{metric}{col}AF&lang={lang}&format={format}'
ERR_MSG = 'Error: could not reach the service. Status code: {}.'
CONN_ERR = 'Error: connection not available.'
FORECAST_HELP = 'Shows also the forecasts for today and tomorrow.'
METRIC_HELP = 'Use the International System of Units.'
USCS_HELP = 'Use the United States Customary Units.'
LANG_HELP = 'Choose preferred language. ISO 639-1 code.'
COLORS_HELP = 'Keep or remove terminal sequences for colors. Default is keep.'
ONELINE_HELP = 'Shorter summary that fits in one line and uses emojis.'
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def default_lang():
    """
    Gets default language ISO 639-1 code.
    """
    return locale.getdefaultlocale()[0][:2]


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('location', default='')
@click.option('-f', '--forecast', is_flag=True, help=FORECAST_HELP)
@click.option('-m', '--metric', 'metric', flag_value='m', help=METRIC_HELP)
@click.option('-u', '--uscs', 'metric', flag_value='u', help=USCS_HELP)
@click.option('-l', '--language', default=default_lang(), help=LANG_HELP)
@click.option('--colors/--no-colors', default='True', help=COLORS_HELP)
@click.option('-o', '--one-line', is_flag=True, help=ONELINE_HELP)
def wttr(location, forecast, metric, language, colors, one_line):
    """
    Cli built using wttr.in API
    """
    url = URL.format(
        loc=location,
        fore='2' if forecast else '0',
        metric=metric if metric is not None else '',
        lang=language,
        col='' if colors else 'T',
        format='4' if one_line else ''
    )
    try:
        response = requests.get(url)
        if response.ok:
            print(response.text)
        else:
            print(ERR_MSG.format(response.status_code))
    except requests.exceptions.ConnectionError:
        print(CONN_ERR)


if __name__ == '__main__':
    wttr()
