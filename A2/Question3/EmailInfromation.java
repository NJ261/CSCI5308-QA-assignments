public class EmailInfromation{

  ProfitReport ProfitReport = new ProfitReport();

  public void SendToEmail(String emailAddress)
  {
    try
    {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < ProfitReport.reportData.size(); i++)
        {
          builder.append(ProfitReport.reportData.get(i) + "\n");
        }
        EmailSender sender = new EmailSender();
        sender.SendEmail(emailAddress, "Profit Report!", builder.toString());
    }
    catch (Exception e)
    {
      System.out.println("Yipes internet must be down!");
    }
  }
}
