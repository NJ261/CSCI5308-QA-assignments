public class SaveOperation{

  PiggyBank PiggyBank = new PiggyBank();

  public void Save()
	{
		try
		{
			PrintWriter writer = new PrintWriter("piggybank.txt", "UTF-8");
			writer.println(Integer.toString(PiggyBank.numPennies));
			writer.println(Integer.toString(PiggyBank.numDimes));
			writer.println(Integer.toString(PiggyBank.numNickels));
			writer.println(Integer.toString(PiggyBank.numQuarters));
			writer.close();
		}
		catch (Exception e)
		{
			System.out.println("I am a bad programmer that hid an exception.");
		}
	}
}
