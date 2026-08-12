package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppTest {
    @Test
    public void testAppGreeting() {
        assertEquals("Hello Jenkins", App.getGreeting());
    }
}
