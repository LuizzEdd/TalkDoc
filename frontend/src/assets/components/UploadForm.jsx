import React, { useState } from "react";

const UploadForm = ({uploadDocument}) => {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (selectedFile) {
            uploadDocument(selectedFile);
            setSelectedFile(null);
        }
    };

    return (
        <form onSubmit = {handleSubmit}>
            <input
            type = "file"
            accept = "application/pdf"
            onChange = {handleFileChange}
            />
            <button type = "submit" disabled = {!selectedFile}>Enviar PDF</button>
        </form>
    );
};

export default UploadForm;