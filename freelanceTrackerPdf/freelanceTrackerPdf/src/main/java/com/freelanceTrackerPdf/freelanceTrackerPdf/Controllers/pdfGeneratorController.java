package com.freelanceTrackerPdf.freelanceTrackerPdf.Controllers;
import com.freelanceTrackerPdf.freelanceTrackerPdf.model.Pdf;
import com.freelanceTrackerPdf.freelanceTrackerPdf.service.pdfGeneratorService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


/*
 pdfGeneratorController class with pdfGeneratorService class object as class variable .
 Initializing it with constructor
Redefining ResponseEntity method to change its default behavior to take https request body as response and don't convert it to json.
it will return ResponseEntity as attachment with pdf as body and media content type will be changed to PDF.
 */
@RestController
public class pdfGeneratorController {
    private final pdfGeneratorService PdfGeneratorService;

    public pdfGeneratorController(pdfGeneratorService PdfGeneratorService){
        this.PdfGeneratorService = PdfGeneratorService;
    }
    @PostMapping("/downloadPdf")
    public ResponseEntity<byte[]> getpdf(@RequestBody Pdf pdf){
        byte[] pdfBytes = PdfGeneratorService.getDetails(pdf);
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_PDF);
        headers.setContentDispositionFormData(
                "attachment", "invoice.pdf"
        );
        return new ResponseEntity<>(pdfBytes, headers, HttpStatus.OK);
    }
}

