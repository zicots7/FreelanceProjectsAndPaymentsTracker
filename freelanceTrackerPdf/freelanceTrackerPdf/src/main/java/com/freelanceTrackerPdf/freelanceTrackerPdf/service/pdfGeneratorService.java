package com.freelanceTrackerPdf.freelanceTrackerPdf.service;
import com.freelanceTrackerPdf.freelanceTrackerPdf.model.Pdf;
import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.element.Paragraph;
import org.springframework.stereotype.Service;
import java.io.ByteArrayOutputStream;

// Made a Pdf generator service class
@Service
public class pdfGeneratorService {
/*
This method getDetails will return Byte array as output and takes pdf class object as input.
Inside try block ByteArrayOutputStream class object as pdfbaos is defined.
Defined a PdfWrite class object which takes a ByteArrayOutputStream object as constructor parameter.
Defined a PdfDocument class object which takes a PdfWriter class object as constructor parameter.
Defined a Document class object which takes a PdfDocument object as constructor parameter.
Calling Document class add method with a Paragraph class object which has user request data as constructor parameter input.
Returns ByteArrayOutputStream object after converting to array
 */
    public byte[] getDetails(Pdf data){

        try {
            ByteArrayOutputStream pdfbaos = new ByteArrayOutputStream();
            PdfWriter writer = new PdfWriter(pdfbaos);
            PdfDocument pdf = new PdfDocument(writer);
            Document document = new Document(pdf);
            document.add(new Paragraph("Project Invoice").setBold().setFontSize(50));
            document.add(new Paragraph("---------------------------------------------------------"));
            document.add(new Paragraph("Client Name: " + data.getClientName()).setFontSize(30));
            document.add(new Paragraph("Project Name: " + data.getProjectName()).setFontSize(30));
            document.add(new Paragraph("Project Description: " + data.getProjectDescription()).setFontSize(30));
            document.add(new Paragraph("Amount: " + data.getAmount()).setFontSize(30));
            document.add(new Paragraph("Date: " + data.getDate()).setFontSize(30));
            document.add(new Paragraph("----------------------------------------------------------"));
            document.add(new Paragraph("Thank You for Choosing Me, Have a Great day!").setFontSize(40));
            document.close();
            return pdfbaos.toByteArray();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }


}
