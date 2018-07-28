import java.util.HashMap;

public class Help
{
	private BaseCommand createCommandBuilder(String command) {	
		HashMap<String, BaseCommand> commands = new HashMap<String, BaseCommand>();
		commands.put("print", new PrintCommand());
		commands.put("open", new  OpenCommand());
		commands.put("close", new CloseCommand());
		return commands.get(command);
	}
	
	public String GetHelp(String command)
	{
		if (command != null && command.length() != 0)
		{
			return createCommandBuilder(command).getCommand();
		}
		return ListAllCommands();
	}

	public String ListAllCommands()
	{
		return "Commands: print, open, close";
	}
}