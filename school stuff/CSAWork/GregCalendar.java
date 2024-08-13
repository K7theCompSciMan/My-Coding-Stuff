import java.util.Calendar;
import java.util.GregorianCalendar;

public class GregCalendar {
        public static void main(String[] args) {
                GregorianCalendar cal = new GregorianCalendar();
                cal.add(Calendar.DAY_OF_MONTH, 100);
                System.out.println("Date: " + cal.getTime() + " WeekDay: " + cal.get(Calendar.DAY_OF_WEEK));
                GregorianCalendar birthday = new GregorianCalendar(2023,Calendar.DECEMBER, 20);
                System.out.println("Weekday of my birthday: " + birthday.get(Calendar.DAY_OF_WEEK));
                birthday.add(Calendar.DAY_OF_MONTH, 10000);
                System.out.println("10,000 days from my birthday is " + birthday.getTime());
        }
}
