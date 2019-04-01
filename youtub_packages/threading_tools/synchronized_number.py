#
# synchronized_number.py
# An implementation of a thread-safe number in Python
#

import threading
from lock_acquisition_exception import LockAcquisitionException


class SynchronizedNumber:
    """
    An implementation of a threadsafe, synchronized number in Python
    """

    def __init__(self, initial_value, should_block_thread=True):
        self.should_block_thread = should_block_thread
        self._lock = threading.Lock()
        self.value = 0
        self.set_value(initial_value)

    def set_value(self, new_value):
        """
        Sets the value of this number.

        :param: new_value - The value to set
        :return: True if value is successfully set, False if not.
        """
        return self.operate_if_satisfies_condition(lambda x: new_value, lambda x: True)

    def increment(self, incr_value):
        """
        Increments the value of this number.

        :param: incr_value - The value to increment by
        :return: True if value is incremented successfully, False if not.
        """
        return self.increment_if_satisfies_condition(incr_value, lambda x: True)

    def decrement(self, decr_value):
        """
        Decrements the value of this number.

        :param: decr_value - The value to decremented by
        :return: True if value is decremented successfully, False if not.
        """
        return self.increment(-decr_value)

    def increment_if_less_than(self, incr_value, limit, eq_ok=False):
        """
        Increments the value of this number only if this number is less than `limit`.

        :param: incr_value - The value to increment by
        :param: eq_ok [optional] - If set to True, the function also allows incrementation if this
                                   number was equal to the `limit`
        :return: True if value is incremented successfully, False if not.
        """

        def does_satisfy(val):
            return val < limit or (eq_ok and val == limit)

        return self.increment_if_satisfies_condition(incr_value, does_satisfy)

    def decrement_if_greater_than(self, decr_value, limit, eq_ok=False):
        """
        Increments the value of this number only if this number is greater than `limit`.

        :param: decr_value - The value to increment by
        :param: eq_ok [optional] - If set to True, the function also allows incrementation if this
                                   number was equal to the `limit`
        :return: True if value is incremented successfully, False if not.
        """

        def does_satisfy(val):
            return val > limit or (eq_ok and val == limit)

        return self.decrement_if_satisfies_condition(decr_value, does_satisfy)

    def increment_if_satisfies_condition(self, incr_value, satisfaction_condition):
        """
        Increments the value of this number only if this number satisfies `satisfaction_condition`.

        :param: incr_value - The value to increment by
        :param: satisfaction_condition - A function that takes in the current value and returns
                                         True if the condition you want is satisfied, and False
                                         otherwise

        :return: True if value is incremented successfully, False if not.
        """
        def iadd_operator(val):
            return val + incr_value

        return self.operate_if_satisfies_condition(iadd_operator, satisfaction_condition)

    def decrement_if_satisfies_condition(self, decr_value, satisfaction_condition):
        """
        Decrements the value of this number only if this number satisfies `satisfaction_condition`.

        :param: decr_value - The value to decrement by
        :param: satisfaction_condition - A function that takes in the current value and returns
                                         True if the condition you want is satisfied, and False
                                         otherwise

        :return: True if value is decremented successfully, False if not.
        """
        return self.increment_if_satisfies_condition(-decr_value, satisfaction_condition)

    def imultiply_if_satisfies_condition(self, mul_value, satisfaction_condition):
        """
        Multiplies the value of this number by `mul_value` only if this number satisfies
        `satisfaction_condition`. Mutuates this `SynchronizedNumber`; does NOT return a new object.

        :param: mul_value - The value to multiply the value of `self` by
        :param: satisfaction_condition - A function that takes in the current value and returns
                                         True if the condition you want is satisfied, and False
                                         otherwise

        :return: True if value is multipled successfully, False if not.
        """
        def imul_operator(val):
            return val * mul_value

        return self.operate_if_satisfies_condition(imul_operator, satisfaction_condition)

    def idivide_if_satisfies_condition(self, div_value, satisfaction_condition):
        """
        Divides the value of this number by `div_value` only if this number satisfies
        `satisfaction_condition`. Mutuates this `SynchronizedNumber`; does NOT return a new object.

        :param: div_value - The value to divide the value of `self` by
        :param: satisfaction_condition - A function that takes in the current value and returns
                                         True if the condition you want is satisfied, and False
                                         otherwise

        :return: True if value is divided successfully, False if not.
        """
        def idiv_operator(val):
            return val / div_value

        return self.operate_if_satisfies_condition(idiv_operator, satisfaction_condition)

    def operate_if_satisfies_condition(self, operator, satisfaction_condition):
        """
        Mutuates the value of this number according the the `operator` function that is passed in,
        only if this number satisfies `satisfaction_condition`. Mutuates this `SynchronizedNumber`;
        does NOT return a new object.

        :param: operator - A function that takes in the current value and returns the new value to
                           assign to this SyncrhonizedNumber
        :param: satisfaction_condition - A function that takes in the current value and returns
                                         True if the condition you want is satisfied, and False
                                         otherwise

        :return: True if value is multipled successfully, False if not.
        """
        if self._lock.acquire(self.should_block_thread):
            try:
                if satisfaction_condition(self.value):
                    self.value = operator(self.value)
                    return True
                else:
                    return False
            finally:
                self._lock.release()

        return False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, SynchronizedNumber):
            return self.value == other.value
        else:
            return self.value == other

    #
    # Default functions that modify existing SynchronizedNumber object
    #

    def __iadd__(self, other):
        add_value = other if not isinstance(other, SynchronizedNumber) else other.value
        success = self.increment(add_value)
        if not success:
            raise LockAcquisitionException('Unable to acquire lock, so += operation failed')
        return self

    def __isub__(self, other):
        sub_value = other if not isinstance(other, SynchronizedNumber) else other.value
        success = self.decrement(sub_value)
        if not success:
            raise LockAcquisitionException('Unable to acquire lock, so -= operation failed')
        return self

    def __imul__(self, other):
        mul_value = other if not isinstance(other, SynchronizedNumber) else other.value
        success = self.imultiply_if_satisfies_condition(mul_value, lambda x: True)
        if not success:
            raise LockAcquisitionException('Unable to acquire lock, so *= operation failed')
        return self

    def __idiv__(self, other):
        div_value = other if not isinstance(other, SynchronizedNumber) else other.value
        success = self.idivide_if_satisfies_condition(div_value, lambda x: True)
        if not success:
            raise LockAcquisitionException('Unable to acquire lock, so /= operation failed')
        return self

    #
    # Default functions that return a new SynchronizedNumber object
    #

    def __add__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(self.value + other.value)
        else:
            return SynchronizedNumber(self.value + other)

    def __sub__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(self.value - other.value)
        else:
            return SynchronizedNumber(self.value - other)

    def __mul__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(self.value * other.value)
        else:
            return SynchronizedNumber(self.value * other)

    def __div__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(self.value / other.value)
        else:
            return SynchronizedNumber(self.value / other)

    def __neg__(self):
        return SynchronizedNumber(-self.value)

    def __pow__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(self.value ** other.value)
        else:
            return SynchronizedNumber(self.value ** other)

    def __mod__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(self.value % other.value)
        else:
            return SynchronizedNumber(self.value % other)

    #
    # Reverse Operations
    #

    def __rsub__(self, other):
        return -self + other

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rdiv__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(other.value / self.value)
        else:
            return SynchronizedNumber(other / self.value)

    def __rpow__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(other.value ** self.value)
        else:
            return SynchronizedNumber(other ** self.value)

    def __rmod__(self, other):
        if isinstance(other, SynchronizedNumber):
            return SynchronizedNumber(other.value % self.value)
        else:
            return SynchronizedNumber(other % self.value)
