import React, {useState} from "react";
import QuestionForm from "./QuestionForm";
import MessageBubble from "./MessageBubble";
import api from "../api";

const ChatWindow = ({documentId}) => {
    const [messages, setMessages] = useState([]);
    const [status, setStatus] = useState('idle');
    const [error, setError] = useState(null);

    const askQuestion = async (question) => {
        setMessages((prev) => [...prev, {role: 'user', text: question}]);
        setStatus('carregando');
        setError(null);

        try {
            const response = await api.post('/chat', {
                document_id: documentId,
                question: question,
            });

            setMessages((prev) => [
                ...prev,
                {
                    role: 'assistant',
                    text: response.data.answer,
                    sources: response.data.sources,
                },
            ]);
            setStatus('idle');
        } catch (err) {
            console.error("Erro ao perguntar.", err);
            setStatus('erro');
            setError("Não foi possível obter a resposta.");
        }
    };
    return (
        <div>
            <div>
                {messages.map((msg, index) => (
                    <MessageBubble key = {index} message = {msg}/>
                ))}
                {status === 'carregando' && <p>Pensando...</p>}
                {status === 'erro' && <p>{error}</p>}
            </div>


            <QuestionForm askQuestion = {askQuestion} disabled = {!documentId || status === 'carregando'}/>
        </div>
    );
};

export default ChatWindow;
