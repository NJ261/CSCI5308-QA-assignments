public class Main
{
	public static void main(String[] args)
	{
		boolean pass = true;
		Person person = new Person();
		pass = person.IsPersonRob();
		if (pass)
		{
			System.out.println("PASS");
		}
		else
		{
			System.out.println("FAIL");
		}
	}
}