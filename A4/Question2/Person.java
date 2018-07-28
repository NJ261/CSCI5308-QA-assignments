
public class Person
{
	private String name;

	String areaCode;
	String phoneNumber;

	String userName;
	String password;
	private PersonAuthentication personAuthentication = new PersonAuthentication();
	private PersonTelephoneNumber personTelephoneNumber = new PersonTelephoneNumber();
	public Person(String name)
	{
		this.name = name;
	}

	public void SetAreaCode(String areaCode)
	{
		this.areaCode = areaCode;
	}
	public String GetAreaCode()
	{
		return areaCode;
	}
	public void SetPhoneNumber(String phoneNumber)
	{
		this.phoneNumber = phoneNumber;
	}

	public String GetPhoneNumber()
	{
		return personTelephoneNumber.GetPhoneNumber(this);
	}

	
	public void SetLoginCredentials(String userName, String password)
	{
		this.personAuthentication.SetLoginCredentials(this, userName, password);
	}

	public boolean AuthenticateUser()
	{
		return personAuthentication.AuthenticateUser(this);
	}
}