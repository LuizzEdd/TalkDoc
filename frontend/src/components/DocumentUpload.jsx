import React, { useState } from "react";
import UploadForm from "./UploadForm";
import api from "../api";

const DocumentUpload = ({onDocumentReady}) => {
    const [status, setStatus] = useState('idle');
    const [error, setError] = useState(null);

    const uploadDocument = async (file) => {
        setStatus('enviando');
        setError(null);
        try {
            const formData = new FormData();
            formData.append('file', file);

            const response = await api.post('/documents/upload', formData);
            setStatus('idle');
            console.log("resposta do upload: ", response.data);
            onDocumentReady(response.data.document_id);
        } catch (err) {
        console.error("Erro ao enviar o documento.", err);
        setStatus('erro');
        setError('Não foi possível processar o documento.');
        }
    };
    
    return (
        <div>
            <UploadForm uploadDocument = {uploadDocument} />
            {status === 'enviando' && <p>Enviando documento...</p>}
            {status === 'erro' && <p>{error}</p>}
        </div>
    );
};

export default DocumentUpload;
