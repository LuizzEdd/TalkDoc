import React from 'react';

const MessageBubble = ({message}) => {
    const {role, text, sources} = message;

    return (
        <div className = {role === 'user' ? 'message-user' : 'message-assistant'}>
            <p>{text}</p>
            {sources && sources.length > 0 && (
                <div>
                    <p>Fontes: {sources.join(', ')}</p>
                </div>
            )}
        </div>
    );
};

export default MessageBubble;