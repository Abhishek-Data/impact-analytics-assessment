import sys
sys.setrecursionlimit(15000)


class Solution:

    def __init__(self, days, consec_absent_not_allowed):
        """
        The constructor for Solution class.

        Parameters:
           days (int): Number of days
           consec_absent_not_allowed (int): Consecutive days absent not allowed
        """
        self.days = days
        self.consec_absent_not_allowed = consec_absent_not_allowed

    def graduating(self):
        path = []
        pattern = ""

        # not allowed pattern for 4 days i.e. 'AAAA'
        not_allowed_pattern = ''.join(
            [''+'A' for _ in range(self.consec_absent_not_allowed)])

        # Recursive Function call
        # Its update path list i.e. ['AAAAA', 'AAAAP', 'AAAPA', 'AAAPP', 'AAPAA', 'AAPAP', 'AAPPA', 'AAPPP', 'APAAA', 'APAAP', 'APAPA', 'APAPP', 'APPAA', 'APPAP', 'APPPA', 'APPPP', 'PAAAA', 'PAAAP', 'PAAPA', 'PAAPP', 'PAPAA', 'PAPAP', 'PAPPA', 'PAPPP', 'PPAAA', 'PPAAP', 'PPAPA', 'PPAPP', 'PPPAA', 'PPPAP', 'PPPPA', 'PPPPP'] for 5 days
        self._util(self.days, pattern, path)

        ans1 = self.waysToAttendClass(path, not_allowed_pattern)
        ans2 = self.probMissGraduation(path, not_allowed_pattern)
        return f"{ans2}/{ans1}"

    def waysToAttendClass(self, path, not_allowed_pattern):
        """
        The function to find The number of ways to attend classes over N days i.e. Answer 1

        Parameters:
            not_allowed_pattern (string): 'AAAA'
            path (Array): Array with all combinations of attending class over N days

        Returns:
            len(path) - count (int): The number of ways to attend classes over N days.
        """
        n = len(path)
        count = 0
        for i in range(n):
            if self.consec_absent_allowed_flag(path[i], not_allowed_pattern):
                count += 1
        return len(path) - count

    def probMissGraduation(self, path, not_allowed_pattern):
        """
        The function to find The probability that you will miss your graduation ceremony. i.e. Answer 2

        Parameters:
            not_allowed_pattern (string): 'AAAA'
            path (Array): Array with all combinations of attending class over N days

        Returns:
            count (int): The probability that you will miss your graduation ceremony
        """
        count = 0
        for i in path:
            if self.consec_absent_allowed_flag(i, not_allowed_pattern):
                path.remove(i)
        for i in path:
            if i[-1] == 'A':
                count += 1
        return count

    def consec_absent_allowed_flag(self, strng, not_allowed_pattern):
        """
        The function to return True for 'AAAA' present in given string else return False

        Parameters:
            strng (string): all ith element of path array i.e. 'PAPPP'
            not_allowed_pattern (string): 'AAAA'

        Returns:
            True/False (Boolean): True for 'AAAA' present in given string else return False
        """
        chr_count = 0
        n = len(strng)
        for i in range(n):
            if (chr_count == len(not_allowed_pattern)):
                break
            if (strng[i] == not_allowed_pattern[chr_count]):
                chr_count += 1
            else:
                chr_count = 0
        return chr_count >= len(not_allowed_pattern)

    def _util(self, days, pattern, path):
        """
        The function to add all combinations of attending class over N days to path array.

        Parameters:
            days (int): Number of days
            pattern (string): A Empty String
            path (Array): Empty Array, use to store all combinations of attending class over N days

        Returns:
            path (Array): Array with all combinations of attending class over N days
        """
        if days == 0:
            path.append(pattern)
            return
        self._util(days-1, f'{pattern}A', path)
        self._util(days-1, f'{pattern}P', path)


if __name__ == "__main__":
    try:
        days = int(input())
    except ValueError:
        print("'Days' must be of integer type")
    except Exception as e:
        print(e)
    else:
        consec_absent_not_allowed = 4
        solution = Solution(days, consec_absent_not_allowed)
        answer = solution.graduating()
        print(answer)
