package amazonitemsearch;
//package amazonitemsearch;
import java.util.HashMap;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
/**
 *
 * @author Khai
 */
public class AmazonItemSearch {

    private static final String ACCESS_KEY_ID = "AKIAJ34LZKKXRWWVREQA";
    private static final String SECRET_KEY = "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";
    private static final String ENDPOINT = "webservices.amazon.com";

    public static void main(String[] args) {
        SignedRequestsHelper helper;

        try {
            helper = SignedRequestsHelper.getInstance(ENDPOINT, ACCESS_KEY_ID, SECRET_KEY);
        } catch (Exception e) {
            e.printStackTrace();
            return;
        }

        String requestUrl = null;

        Map<String, String> params = new HashMap<String, String>();
        params.put("Service", "AWSECommerceService");
        params.put("Operation", "ItemSearch");
        params.put("AWSAccessKeyId", "AKIAJ34LZKKXRWWVREQA");
        params.put("AssociateTag", "kdhua-20");
        params.put("SearchIndex", "All");
        params.put("Keywords", "chair");
        params.put("ResponseGroup", "ItemAttributes,Offers");
        requestUrl = helper.sign(params);

        System.out.println(requestUrl);

    }
    
}
