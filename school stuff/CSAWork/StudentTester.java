
public class StudentTester 
{ 
        public static void main(String[] args)
        {
                Student student = new Student("John");
                System.out.println(student.getName());
                System.out.println("Expected: John");
                
                student.addQuiz(90);
                System.out.print(student.getTotalScore() + " ");
                System.out.println(student.getAverageScore());
                System.out.println("Expected: 90 90");
                System.out.println("Expected: John");

                student.addQuiz(100);
                System.out.print(student.getTotalScore() + " ");
                System.out.println(student.getAverageScore());
                System.out.println("Expected: 190 95");
        }
}
