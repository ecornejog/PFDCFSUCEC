import datetime


class DateFormat():

    @classmethod
    def convert_date(self, date):
        if (date):
            return datetime.datetime.strftime(date, '"%d/%m/%Y, %H:%M:%S"')
        else:
            return ("still in execution")
