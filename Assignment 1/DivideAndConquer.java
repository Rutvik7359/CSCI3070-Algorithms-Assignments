import java.io.*;
import java.util.Scanner;



public class DivideAndConquer {
	public static void divide(char[] textChars, char[] inputChars, int x1, int x2){
		//System.out.print(textChars[x1] + " ");
		//System.out.print(textChars[x2] + " ");
		
		//Check at start of segment
		if(textChars[x1] == inputChars[0] ){
			//System.out.println("match found, starting attempt to match");
			for(int i = 0; i < inputChars.length; i++){
				if(inputChars[i] == textChars[x1+i]){
					//System.out.print(inputChars[i]);
					if(i == inputChars.length-1){
						System.out.println("Success finding input word.");
						System.exit(0);
					}
				} else {
					break;
				}
			}
		} if (textChars[x2] == inputChars[inputChars.length-1]){
			for(int i = inputChars.length-1; i >= 0; i--){
				//System.out.print(textChars[i]);
				if(inputChars[i] == textChars[i]){
					System.out.print(inputChars[i]);
					System.out.print(i);
					System.exit(0);
				} else {
					break;
				}
			}
		}
		if (x1 < x2){
			int pivot = x2 / 2;
			//System.out.println("Pivot: " + pivot);
			divide(textChars, inputChars, x1, pivot);
			divide(textChars, inputChars, pivot+1, x2-1);
		}
	}
	
	
	public static void main(String args[]) throws FileNotFoundException{
		String s;
		String text = "";
		String find;
		
		System.out.println("This program reads from a text file located in the same directory.");
		System.out.println("Just specify the name of the text file, e.g.: \"textfile.txt\" ");
		Scanner input = new Scanner(System.in);
		s = input.nextLine();
		
		System.out.println(s); //delete later
		
		Scanner read = new Scanner(new File(s));
		while(read.hasNextLine()){
			text += read.nextLine() + "\n";
			//System.out.println(text); //delete later
		}
		char[] textChars = text.toCharArray();
		
		//System.out.println("Textfile length:" + textChars.length);
		//System.out.println(text); //delete later
		
		input = new Scanner(System.in);
		System.out.println("Enter a string to look for: ");
		find = input.nextLine();
		System.out.println("You entered: " + find); //delete later
		char[] findChars = find.toCharArray();
		//System.out.println("TextChars: " + textChars.length);
		
		divide(textChars, findChars, 0, textChars.length - 1);
	}
	

}