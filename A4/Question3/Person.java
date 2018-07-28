public class Person
{
	public String name;
	private Address personAddress;
	public Person()
	{
		name = "Rob";
		personAddress = new Address();
		personAddress.setCity("Rob street");
		personAddress.setPostalCode("Rob street");
		personAddress.setProvince("Rob street");
		personAddress.setStreet("Rob street");	
	}

	public Address getAddress() {
		return personAddress;
	}

	public boolean IsPersonRob()
	{
		return name.equals("Rob") && IsRobsAddress(new Address("Rob street", "Rob street", "Rob street", "Rob street"));
	}

	private boolean IsRobsAddress(Address address)
	{
		return personAddress.getStreet().equals(address.getStreet()) &&
				personAddress.getCity().equals(address.getCity()) &&
				personAddress.getProvince().equals(address.getProvince()) &&
				personAddress.getProvince().equals(address.getProvince());

	}
}