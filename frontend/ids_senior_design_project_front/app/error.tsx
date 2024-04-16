'use client'

import { useEffect } from 'react'

export default function Error({
    error,
    reset,
    }: {
    error: Error & { digest?: string }
    reset: () => void
}) {
    useEffect(() => {
        console.error(error)
    }, [error])
    
    return (
        <div className='flex flex-col h-[400px] items-center justify-center'> 
            <p>Something went wrong!</p>
            <button
                className="text-center mt-10 bg-primary rounded-[5px] h-8 w-24 text-white shadow-lg hover:bg-[#0e5499] transition-colors duration-[400ms]"
                onClick={
                () => reset()
                }
            >
                Try again
            </button>
        </div>
    )
}