class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Case 1: numerator is zero
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)

        # Decimal point
        result.append(".")

        # Map remainder -> position in result
        seen = {}

        while remainder != 0:
            if remainder in seen:
                # Insert parentheses
                idx = seen[remainder]
                result.insert(idx, "(")
                result.append(")")
                break

            seen[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator

        return "".join(result)