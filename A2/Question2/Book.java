import java.time.Duration;
import java.util.ArrayList;

public class Book implements IBookSwitch
{

	public String GetAuthor()
	{
		return "Hemingway";
	}

	public String GetTitle()
	{
		return "For Whom The Bell Tolls";
	}

	public boolean IsDigitalOnly()
	{
		return false;
	}

	public ArrayList<String> GetCastList()
	{
		return null;
	}
}
