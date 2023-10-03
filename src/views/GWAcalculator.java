import java.util.Scanner;

public class GWAcalculator {
	enum Achievement {
        PRESIDENTS_LIST("President's Lister", 1.5f),
        DEANS_LIST("Dean's Lister", 1.75f),
        PASSED("Passed", 3.0f),
        FAILED("Failed", 5.0f);

        private final String label;
        private final float gwaThreshold;

        Achievement(String label, float gwaThreshold) {
            this.label = label;
            this.gwaThreshold = gwaThreshold;
        }

        public String getLabel() {
            return label;
        }

        public float getGwaThreshold() {
            return gwaThreshold;
        }
	}
	
	private static Achievement calculateAchievement(float gwa) {
        for (Achievement achievement : Achievement.values()) {
            if (gwa < achievement.getGwaThreshold()) {
                return achievement;
            }
        }
        return Achievement.PASSED; // Default to PASSED if no other achievement is met
    }
	
	
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Primitive Data Type
        char Gender, userChoice;
        boolean userAction = true;
        double result = 0;

        // Non-primitive Data Type
        String userName, userCourse, userGender, solveExpression;
        

        // User Input and Output
        System.out.print("Enter your Name: ");
        userName = input.nextLine();
        System.out.print("Enter your Gender (M/F): ");
        Gender = input.next().charAt(0);
        input.nextLine();
        System.out.print("Enter your Course: ");
        userCourse = input.nextLine();

        // If Else statement
        if (Gender == 'M') {
            userGender = "Male";
        } else if (Gender == 'F') {
            userGender = "Female";
        } else {
            userGender = "Unknown";
        }
        // do..while
        do {
            System.out.println("----------------------------------------------------------------");
            System.out.println("\n\nHello " + userName + "!!");
            System.out.println("Gender: " + userGender);
            System.out.println("Course: " + userCourse);
            System.out.println("\nWhat do you want to do: \nA. Simple Arithmetic Calculator\nB. GWA Calculator\nC. Exit");
            System.out.print("Your Choice: ");
            userChoice = input.next().charAt(0);

            // switch
            switch (userChoice) {
                case 'A':
                	input.nextLine(); // Consume the newline character
                    // while loop with break
                    while (true) {
                        System.out.println("\nEnter a series of numbers and operations (e.g., 5 * 3 + 2 - 1 / 4) or 'x' to cancel:");
                        solveExpression = input.nextLine();

                        if (solveExpression.equalsIgnoreCase("x")) {
                            break;
                        }

                        try {
                            result = calExpression(result, solveExpression);
                            System.out.println("Answer: " + result);
                        } catch (IllegalArgumentException e) {
                            System.out.println("Invalid input. Try again.");
                        }
                    }
                    break;

                case 'B':
                    System.out.println("---GWA calculator---");
                    input.nextLine();
                    calGWA();
                    break;
                    
                case 'C':
                	userAction = false;
                	break;
                	
                default:
                	System.out.println("\n-----Wrong Input! Try Again-----");
            }
        } while (!userAction);

        System.out.println("\n\nThank You! \nProgram Ended!");
        input.close();
    }

    private static Double calExpression(double solResult, String inputExp) {
        String[] parts = inputExp.split(" ");
        double integer = Double.parseDouble(parts[0]);
        solResult = integer;
        String operations = "";

        for (int i = 1; i < parts.length; i += 2) {
            operations = parts[i];
            double nextNum = Double.parseDouble(parts[i + 1]);

            switch (operations) {
                case "+":
                    solResult += nextNum;
                    break;
                case "-":
                    solResult -= nextNum;
                    break;
                case "*":
                    solResult *= nextNum;
                    break;
                case "/":
                    if (nextNum != 0) {
                        solResult /= nextNum;
                    } else {
                        throw new IllegalArgumentException("Division by zero is not allowed.");
                    }
                    break;
                default:
                    throw new IllegalArgumentException("Invalid operator: " + operations);
            }
        }
        return solResult;
    }
    
    private static void calGWA() {
        Scanner input = new Scanner(System.in);
        String[][] userGrade;
        float numGrade;
        int numSubject;
        
        while (true) {
            System.out.print("Enter the number of Subjects: ");
            numSubject = input.nextInt();
            // Consume the newline character left in the buffer
            input.nextLine();
            
            userGrade = new String[numSubject][3]; // Initialize the userGrade array
            System.out.println("Enter the Subject, Unit and Grade (e.g. 'Introduction_to_Computing 3 1.25'): ");
            System.out.println("Note: Add underscore to the spaces in course title ");
            for (int i = 0; i < numSubject; i++) {
            	System.out.print(i+1 + ". ");
                String userInput = input.nextLine();
                userGrade[i] = userInput.split(" ");
            }
            
            // Calculate GWA based on the user's input
            float totalGrade = 0;
            int totalUnits = 0;
            
            for (int i = 0; i < numSubject; i++) {
                int units = Integer.parseInt(userGrade[i][1]);
                float grade = Float.parseFloat(userGrade[i][2]);
                totalGrade += units * grade;
                totalUnits += units;
            }
            
            float gwa = totalGrade / totalUnits;
            System.out.println("\nYour Grade Weighted Average (GWA) is: " + gwa);
            
            Achievement achievement = calculateAchievement(gwa);
            System.out.println("Your Achievement: " + achievement.getLabel());
            
            System.out.print("\nDo you want to calculate GWA again? (yes/no): ");
            String response = input.nextLine();
            
            if (!response.equalsIgnoreCase("yes")) {
                break; // Exit the loop if the user doesn't want to calculate GWA again
            }
        }
        
        input.close();
    }
}
