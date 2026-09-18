import React from 'react';
import ReactMarkdown from 'react-markdown';

const MessageBubble = ({message}) => {
    const {role, text, sources} = message;

    return (
        <div className = {role === 'user' ? 'message-user' : 'message-assistant'}>
            {role === 'assistant' ? (
                <ReactMarkdown>{text}</ReactMarkdown>
            ) : (
                <p>{text}</p>
            )}
            {sources && sources.length > 0 && (
                <div>
                    <p>Fontes: {sources.join(', ')}</p>
                </div>
            )}
        </div>
    );
};

export default MessageBubble;