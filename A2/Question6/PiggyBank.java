import java.io.*;
import java.util.Scanner;

public class PiggyBank
{
	int numPennies;
	int numDimes;
	int numNickels;
	int numQuarters;

	public PiggyBank()
	{
		numPennies = 0;
		numDimes = 0;
		numNickels = 0;
		numQuarters = 0;
	}

	public void AddPenny()
	{
		numPennies += 1;
	}

	public void AddDime()
	{
		numDimes += 1;
	}

	public void AddNickel()
	{
		numNickels += 1;
	}

	public void AddQuarter()
	{
		numQuarters += 1;
	}

}
