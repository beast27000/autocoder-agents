import React from 'react';

interface LoadingStateProps {
  agents: string[];
  currentAgent: string;
}

export const LoadingState: React.FC<LoadingStateProps> = ({ agents, currentAgent }) => {
  return (
    <div className="w-full max-w-2xl mx-auto mt-8 p-6 bg-white rounded-lg shadow-lg">
      <div className="space-y-4">
        <h3 className="font-semibold text-gray-800">Agents Processing...</h3>
        <div className="space-y-2">
          {agents.map((agent) => (
            <div
              key={agent}
              className={`p-3 rounded-lg flex items-center gap-3 ${
                currentAgent === agent
                  ? 'bg-blue-100 border-l-4 border-blue-500'
                  : 'bg-gray-100'
              }`}
            >
              <div
                className={`w-3 h-3 rounded-full ${
                  currentAgent === agent ? 'bg-blue-500 animate-pulse' : 'bg-gray-300'
                }`}
              />
              <span
                className={`text-sm font-medium ${
                  currentAgent === agent ? 'text-blue-700' : 'text-gray-600'
                }`}
              >
                {agent}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
