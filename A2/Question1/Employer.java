import java.util.ArrayList;

public class Employer
{
	private IEmployerInterface IEmployerInterface;
	ArrayList<IEmployerInterface> workers;

	public Employer()
	{
		workers = new ArrayList<IEmployerInterface>();
		for (int i = 0; i < 5; i++)
		{
			workers.add(new HourlyWorker());
		}
		for (int i = 0; i < 5; i++)
		{
			workers.add(new SalaryWorker());
		}
	}

	public void outputWageCostsForAllStaff(int hours)
	{
		float cost = 0.0f;
		for (int i = 0; i < workers.size(); i++)
		{
			IEmployerInterface worker = workers.get(i);
			cost += worker.calculatePay(hours);
		}

		System.out.println("Total wage cost for all staff = $" + cost);
	}
}
