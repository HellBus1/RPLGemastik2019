package com.example.proyekmingguan;

public class DataPart {
    private String fileName;
    private byte[] content;
    private String type;

    DataPart() {
    }

    DataPart(String name, byte[] data) {
        fileName = name;
        content = data;
    }

    String getFileName() {
        return fileName;
    }

    byte[] getContent() {
        return content;
    }

    String getType() {
        return type;
    }
}
