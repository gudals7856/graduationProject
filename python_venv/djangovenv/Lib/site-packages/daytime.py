import time
import datetime


class Daytime(datetime.time):
    """
    Compare, add or substract daytimes.
    
    This module extends the datetime.time-module and makes it more handy
    respectivly to comparison, addition and substraction.
    You can compare, add and substract a daytime-object with other daytime-objects
    or with an integer as the amount of seconds. You can also compare a daytime-
    with a datetime.time-object.

    Attributes:
        delta:          daytime as datetime.timedelta-instance
        total_seconds:  daytime in seconds as a float

    """
    @classmethod
    def fromtime(cls, time):
        """
        Build a daytime from a datetime.time- or datetime.datetime-object.
        
        Args:
            time:   datetime.time- or datetime.datetime-object

        Returns a daytime.
        """
        return cls(
            hour=time.hour,
            minute=time.minute,
            second=time.second,
            microsecond=time.microsecond
            )

    @classmethod
    def strptime(cls, string, format):
        """
        Build a daytime from a string and a format.

        Args:
            string:     string parsed according to the specified format
            format:     See the library reference manual for formatting codes.
        
        Returns a daytime.

        """
        return cls.fromtime(datetime.datetime.strptime(string, format))

    @classmethod
    def fromtimestamp(cls, timestamp):
        """
        Build a local daytime from timestamp.

        Args:
            timestamp:    a POSIX timestamp, such as is returned by time.time()

        Returns a daytime.

        """
        return cls.fromtime(datetime.datetime.fromtimestamp(timestamp))

    @classmethod
    def utcfromtimestamp(cls, timestamp):
        """
        Build a utc-daytime from timestamp.

        Args:
            timestamp:    a POSIX timestamp, such as is returned by time.time()

        Returns a daytime.

        """
        return cls.fromtime(datetime.datetime.utcfromtimestamp(timestamp))

    @classmethod
    def daytime(cls):
        """
        Returns the actual daytime.
        """
        return cls.fromtime(datetime.datetime.today())

    @property
    def as_timedelta(self):
        """
        Daytime as timedelta.
        """
        return datetime.timedelta(
            hours=self.hour,
            minutes=self.minute,
            seconds=self.second,
            microseconds=self.microsecond
            )

    @property
    def as_seconds(self):
        """
        Absolute amount of seconds of the daytime.
        """
        return self.as_timedelta.total_seconds()

    def __add__(self, other, sign=1):
        if isinstance(other, int) or isinstance(other, float):
            seconds = self.as_seconds + sign * other
        elif isinstance(other, Daytime):
            seconds = self.as_seconds + sign * other.as_seconds
        elif isinstance(other, datetime.time):
            seconds = self.as_seconds + sign * Daytime.fromtime(other).as_seconds
        elif isinstance(other, datetime.timedelta):
            seconds = self.as_seconds + sign * other.total_seconds()
        else: raise TypeError("unsupported operator for Daytime and {0}".format(
            other.__class__.__name__))

        return Daytime.utcfromtimestamp(seconds)

    def __sub__(self, other):
        return self.__add__(other, -1)

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.as_seconds > other
        else: return super(Daytime, self).__gt__(other)

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.as_seconds >= other
        else: return super(Daytime, self).__ge__(other)

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.as_seconds < other
        else: return super(Daytime, self).__lt__(other)

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.as_seconds <= other
        else: return super(Daytime, self).__le__(other)

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.as_seconds == other
        else: return super(Daytime, self).__eq__(other)

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.as_seconds != other
        else: return super(Daytime, self).__ne__(other)


