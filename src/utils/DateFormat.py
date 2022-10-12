from datetime import datetime


class DateFormat():

    @classmethod
    def convert_date(self, date):
        if (date):
            return datetime.strftime(date, '%d/%m/%Y,%H:%M:%S')
        else:
            return ("NULL")


    @classmethod
    def deltaTime(self,date1,date2):
               


                t1 = datetime.strptime(date1, "%d/%m/%Y,%H:%M:%S")
                print('Start time:', t1.time())

                t2 = datetime.strptime(date2, "%d/%m/%Y,%H:%M:%S")
                print('End time:', t2.time())


                delta = t2 - t1

                print(f"Time difference is {delta.total_seconds()} seconds")

                return delta.total_seconds()

