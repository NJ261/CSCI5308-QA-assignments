public class PersonTelephoneNumber {
	public PersonTelephoneNumber() {
		// TODO Auto-generated constructor stub
	}

	public String GetPhoneNumber(Person person)
	{
		if (person.areaCode != null && person.areaCode != "")
		{
			return "(" + person.areaCode + ") " + person.phoneNumber; 
		}
		return person.phoneNumber;
	}

}
