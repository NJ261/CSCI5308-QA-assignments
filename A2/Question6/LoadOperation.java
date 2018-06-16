public class LoadOperation{

	PiggyBank PiggyBank = new PiggyBank();

	public void Load()
	{
		try
		{
			Scanner in = new Scanner(new FileReader("piggybank.txt"));
			PiggyBank.numPennies = Integer.parseInt(in.next());
			PiggyBank.numDimes = Integer.parseInt(in.next());
			PiggyBank.numNickels = Integer.parseInt(in.next());
			PiggyBank.numQuarters = Integer.parseInt(in.next());
		}
		catch (Exception e)
		{
			System.out.println("I am a bad programmer that hid an exception.");
		}
	}
}
