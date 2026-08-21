import { useState } from 'react';
import DocumentUpload from "./assets/components/DocumentUpload";
import ChatWindow from './assets/components/ChatWindow';

const App = () => {
  const [documentId, setDocumentId] = useState(null);

  console.log(documentId)
  return (
    <div>
      <DocumentUpload onDocumentReady = {setDocumentId}/>
      <ChatWindow documentId = {documentId}/>
    </div>
  );
};

export default App;
