import globalVars
import pycurl
import json
from io import BytesIO
from yahoo_finance import Currency
from datetime import datetime
#from dateparser import parse


def getShare(identifier):
    try:
        get_value_url = 'http://finance.google.com/finance/info?client=ig&q=' + identifier
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, get_value_url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        value = buffer.getvalue()
        value = value.decode('utf-8')
        print(value)
        j = json.loads(value[5:len(value) - 2])
        share_value = float(j['l'].replace(',', ''))
        share_lastDayClose = float(j['pcls_fix'])
        share_change = ((share_value / share_lastDayClose) -1) * 100  # El resultado se devuelve en %
        dt = j['lt_dts']
        dt = dt[:-1]
        share = {'Name': j['t'], 'Index': j['e'], 'Open': j['pcls_fix'], 'Value': share_value, 'Datetime': dt, 'Change': share_change, 'LastDayClose': share_lastDayClose}
        return share
    except Exception as e:
        globalVars.toLogFile('Error getShare: ' + str(e))
        return None


def getCurrency(identifier):
    try:
        result = Currency(identifier)
        dt = result.get_trade_datetime()[:-9]
        currency = {'Name': identifier, 'Value': result.get_rate(), 'Datetime': dt}
        return currency
    except Exception as e:
        globalVars.toLogFile('Error getCurrency: ' + str(e))
        return None


# if __name__ == "__main__":
#     company = 'BME:TEF'
#     share = getShare(company)
#     if share:
#         print('Ticker: ' + share['Name'])
#         print('UltimoValor: %.2f' % share['LastDayClose'])
#         print('Actual: %.2f' % share['Value'])
#         print('Fecha: ' + share['Datetime'])
#         print('Var: %.2f' % share['Change'] + '%')
