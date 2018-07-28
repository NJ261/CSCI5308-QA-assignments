public class PersonAuthentication {

	public PersonAuthentication() {
	}

	public boolean AuthenticateUser(Person person)
	{
		return (person.userName.equals("joe") && person.password.equals("joepass"));
	}

	public void SetLoginCredentials(Person person, String userName, String password)
	{
		person.userName = userName;
		person.password = password;
	}

}
