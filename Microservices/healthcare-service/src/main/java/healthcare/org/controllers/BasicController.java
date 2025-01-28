package healthcare.org.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/data")
public class BasicController {
    @GetMapping
    public String hello() {
        return "Hello World";
    }
}
