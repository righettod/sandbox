package eu.righettod;

import javax.xml.XMLConstants;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import java.io.File;
import java.util.Arrays;
import java.util.List;

public class Sandbox {
    public static void main(String[] args) throws Exception {
        System.out.printf("Java version: %s\n", System.getProperty("java.version"));
        SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        //See https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html
        //factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
        List<String> testFiles = Arrays.asList("test1.xsd", "test2.xsd");
        testFiles.forEach(f -> {
            try {
                System.out.printf("[+] File '%s\n", f);
                Schema schema = factory.newSchema(new File(f));
            } catch (Exception e) {
                System.out.printf("Error: %s\n", e.getMessage());
            }
        });
    }
}
