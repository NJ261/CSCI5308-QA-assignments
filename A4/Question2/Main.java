public class Main
{
	public static void main(String[] args)
	{
		boolean pass = true;
		Person person = new Person("joe");
		person.SetAreaCode("902");
		person.SetPhoneNumber("123-4567");
		person.SetLoginCredentials("joe", "joepass");
		pass = person.GetPhoneNumber().equals("(902) 123-4567") && person.AuthenticateUser();
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