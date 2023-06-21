import React from 'react'
import { useNavigate } from 'react-router'

const Header = () => {
	const navigate = useNavigate();
	return (
		<div className='bg-transparent shadow-white p-4 shadow-sm px-16'>
			<h1 className='mx-auto text-2xl font-semibold text-left text-white' onClick={() => navigate("/")}>Wrangle <span className=' bg-clip-text text-transparent bg-gradient-to-br font-extrabold to-pink-300 from-blue-600 text-4xl'>.</span></h1>
		</div>
	)
}

export default Header