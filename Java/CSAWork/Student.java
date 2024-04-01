public class Student 
{
      private String name;
      private int totalQuizScore;
      private int numberOfQuizzes;
      
      public Student(String name) 
      {
                this.name = name;
                this.totalQuizScore = 0;
      }
      public String getName() 
      {
                return this.name;
      }
      public void addQuiz(int score) 
      {
                this.totalQuizScore = this.totalQuizScore + score;
                this.numberOfQuizzes = this.numberOfQuizzes + 1;
      }
      public int getTotalScore() 
      {
                return this.totalQuizScore;
      }
      public double getAverageScore() 
      {
                return this.totalQuizScore / numberOfQuizzes;
      }
      
}
