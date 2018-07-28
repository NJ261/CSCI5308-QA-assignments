public class Main
{
	public static void main(String[] args)
	{
		Help help = new Help();
		boolean pass = help.GetHelp("").equals("Commands: print, open, close") &&
			help.GetHelp("print").equals("print -f <path> [-colour=0/1] [-two-sided=0/1]") &&
			help.GetHelp("open").equals("open -f <path> [-create=0/1]") &&
			help.GetHelp("close").equals("close -f <path>");
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