public class  StringToIntegerAtoi {
    public int myAtoi(String str) {
        str = str.trim();
        if (str.isEmpty()) return 0;
        int sign = 1;
        int index = 0;
        if (str.charAt(0) == '-') {
            sign = -1;
            index++;
        } else if (str.charAt(0) == '+') {
            index++;
        }
        long num = 0;
        while (index < str.length() && Character.isDigit(str.charAt(index))) {
            num = num * 10 + (str.charAt(index) - '0');
            if (num > Integer.MAX_VALUE) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            index++;
        }
        return (int) (num * sign);
    }
}