public class Person 
{
	public String name;
	public String street; 
	public String city;
	public String province;
	public String postalCode;
	
	Address address;

	public Person()
	{
		address = new Address("Rob street", "Rob city", "Rob province", "Rob postalcode");
		name = "Rob";
	}

	public boolean IsPersonRob()
	{
		return name.equals("Rob") && IsRobsAddress(address);
	}

	private boolean IsRobsAddress(Address address)
	{
		return address.getStreet().equals("Rob street") &&
			address.getCity().equals("Rob city") &&
			address.getProvince().equals("Rob province") &&
			address.getPostalCode().equals("Rob postalcode");
	}
}
