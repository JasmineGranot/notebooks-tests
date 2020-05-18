# code tested on the following patbas
# def join(*args, sep='-'):
#     to_return = []
#     for arg in args[:-1]:
#         to_return.extend(arg)
#         to_return.append(sep)
#     to_return.extend(args[-1])
#     return to_return


class TestJoin:
    """Cup of join"""

    def test_join(self):
        """בדיקת פונקציה join"""
        method_here = 'join' in globals()
        assert method_here, 'חסרה המתודה join'
        assert join([1, 2], [8], [9, 5, 6], sep='@') == [1, 2, '@', 8, '@', 9, 5, 6]
        assert join([1, 2], [8], [9, 5, 6], sep='*~*') == [1, 2, '*~*', 8, '*~*', 9, 5, 6]
        assert join([1, 2], [8], [9, 5, 6]) == [1, 2, '-', 8, '-', 9, 5, 6]
        assert join([1]) == [1]

        try:
            assert join() is None
        except AssertionError:
            raise
        except Exception:
            pass
