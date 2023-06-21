import React from 'react'
import { useNavigate } from 'react-router';

const LandingPage = () => {
	const navigate= useNavigate();
  return (
	<div className="bg-home h-screen">
		<div className='bg-black p-4 shadow-md px-16 flex justify-between '>
			<h1 className=' text-2xl text-white font-semibold text-left'> Wrangle.</h1>
			<button onClick={() => navigate("/home")} className='text-transparent border bg-clip-border  border-pink-200 text-white px-6 rounded-md'>Home</button>
		</div>
		<div className='w-[70%] mt-20 px-16'>
			<h1 className='text-[3.5rem] text-white font-semibold text-left'>Ultra-Realistic and Affordable Text-to-Speech BOT</h1>
			<p className='text-left text-gray-300 text-2xl pt-2 w-[65%]'>Experience lifelike speech synthesis at an unbeatable value with no cost at all</p>
		</div>
		<div className='text-left px-16 mt-8'>
			<button onClick={() => navigate("/home")} className='bg-gradient-to-l to-pink-300 from-blue-600 px-6 py-2 rounded-xl font-semibold text-white'>Try bot for free</button>
		</div>
	</div>

  )
}

export default LandingPage