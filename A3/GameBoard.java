import java.io.IOException;
import java.util.*;
import java.nio.file.*;

// This is the Singleton that implements the game, it glues all the patterns together.
public class GameBoard
{
	// The ONE instance of GameBoard.
	private static GameBoard instance = null;
	
	private  ArrayList<ArrayList<BoardComponent>> board;
	private final IAsteroidGameFactory factory;
	private int buildingCount;
	private IState gameState;
	
	// The one way to get the Singleton
	public static GameBoard Instance()
	{
		if (null == instance)
		{
			instance = new GameBoard();
		}
		return instance;
	}
	
	private GameBoard()
	{
		board = null;
		factory = new AsteroidGameFactory();
		buildingCount = 0;
		gameState = new SetupState();
	}
	
	public ArrayList<ArrayList<BoardComponent>> GetBoard()
	{
		return board;
	}
	
	public void SetBoard(ArrayList<ArrayList<BoardComponent>> board)
	{
		this.board = board;
	}
	
	public IAsteroidGameFactory GetFactory()
	{
		return factory;
	}
	
	public void ProcessCommands(String commandFileName)
	{
		try
		{
			List<String> commandLines = Files.readAllLines(Paths.get(commandFileName));
			Iterator<String> iter = commandLines.iterator();
			while (iter.hasNext())
			{
				String commandLine = iter.next();
				Command command = factory.MakeCommand(commandLine);
				if (command != null)
				{
					command.Execute();
				}
				// After every command check whether the game is over!
				if (gameState.IsGameOver())
				{
					// Game over, stop processing commands even if there are some left
					System.out.println("GAME OVER!!");
					break;
				}
			}
		}
		catch (IOException e)
		{
			System.out.println("Failed to parse command file: " + e.getMessage());
		}
	}
	
	// This tells all the components in the board composite to perform
	// their Operation()
	public void DoTick()
	{
		for (int i = 0; i < board.size(); i++)
		{
			ArrayList<BoardComponent> row = board.get(i);
			for (int j = 0; j < row.size(); j++)
			{
				BoardComponent square = row.get(j);
				square.Operation();
			}
		}
	}
	
	// Increment the building count.
	public void IncrementBuildingCount()
	{
		buildingCount += 1;
	}
	
	// Decrement the building count.
	public void DecrementBuildingCount()
	{
		buildingCount -= 1;
	}
	
	public int GetBuildingCount()
	{
		return buildingCount;
	}
	
	// Start the game.
	public void StartGame()
	{
		gameState = new GameState();
	}
}
