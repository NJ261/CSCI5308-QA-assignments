import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import javax.print.Doc;
import javax.print.DocFlavor;
import javax.print.DocPrintJob;
import javax.print.PrintException;
import javax.print.PrintService;
import javax.print.PrintServiceLookup;
import javax.print.SimpleDoc;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
import javax.print.attribute.standard.Copies;
import javax.print.event.PrintJobAdapter;
import javax.print.event.PrintJobEvent;
import java.util.ArrayList;

public class ProfitReport
{
	private ArrayList<String> reportData;

	public ProfitReport()
	{
		reportData = new ArrayList<String>();
	}

	public void CreateReport()
	{
		reportData.add("Canada made $100000");
		reportData.add("Mexico made $1007700");
		reportData.add("Russia made $10009940");
		reportData.add("India made $10004500");
		reportData.add("China made $1045460000");
		reportData.add("Iran made $100466000");
		reportData.add("England made $1006000");
		reportData.add("Germany made $133300000");
		reportData.add("Chile made $1000400");
	}

}
