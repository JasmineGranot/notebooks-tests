# code tested on the following patbas
# def avg(*args):
#     return sum(args) / len(args)


class TestAvg:
    """כפלו לי שתו לי"""

    def test_avg(self):
        """בדיקת פונקציה avg"""
        method_here = 'avg' in globals()
        assert method_here, 'חסרה המתודה avg'
        assert avg(5, 6) == 5.5
        assert avg(3, 5, 10) == 6
        assert avg(2) == 2
        try:
            assert avg() is None
        except AssertionError:
            raise
        except Exception:
            pass
