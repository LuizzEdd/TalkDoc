import React, {useState} from "react";

const QuestionForm = ({askQuestion, disabled}) => {
    const [question, setQuestion] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        if (question.trim()) {
            askQuestion(question);
            setQuestion('');
        }
    };
    
    return (
        <form onSubmit = {handleSubmit}>
            <input
                type = 'text'
                value = {question}
                onChange = {(e) => setQuestion(e.target.value)}
                placeholder = "Pergunte sobre o documento."
                disabled = {disabled}
            />
            <button type ="submit" disabled = {disabled || !question.trim()}>Enviar</button>
        </form>
    );
};

export default QuestionForm;