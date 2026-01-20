declare module 'react-syntax-highlighter' {
  import React from 'react';
  
  interface SyntaxHighlighterProps {
    language?: string;
    style?: any;
    children?: React.ReactNode;
    className?: string;
    [key: string]: any;
  }

  const SyntaxHighlighter: React.FC<SyntaxHighlighterProps>;
  export default SyntaxHighlighter;
}

declare module 'react-syntax-highlighter/dist/esm/styles/hljs' {
  export const atomOneDark: any;
  export const atomOneLight: any;
  [key: string]: any;
}