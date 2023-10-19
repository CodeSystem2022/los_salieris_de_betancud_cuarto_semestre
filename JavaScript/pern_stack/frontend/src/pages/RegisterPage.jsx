import React from "react";
import { useForm } from "react-hook-form";

import { Card, Input, Button } from "../components/ui";

const RegisterPage = () => {
  const { register, handleSubmit, formState: {errors} } = useForm()

  const onSubmit = handleSubmit(data => {
    console.log(data);
  })

  console.log(errors);

  return (
    <div className="h-[calc(100vh-64px)] flex items-center justify-center">
      <Card>
        <h3 className="text-2xl font-bold">Registro</h3>
        <form onSubmit={onSubmit}>
          <Input
            placeholder="Ingrese su nombre"
            { ...register('name', { required: true }) }
          /> 
          { errors.name
            ? <span className="text-red-500">Este campo es requerido</span>
            : null
          }
          <Input
            type="email"
            placeholder="Ingrese su email"
            { ...register('email', { required: true }) }
          />
          { errors.email
            ? <span className="text-red-500">Este campo es requerido</span>
            : null
          }
          <Input
            type="password"
            placeholder="Ingrese su contraseña"
            { ...register('password', { required: true }) }
          />
          { errors.password
            ? <span className="text-red-500">Este campo es requerido</span>
            : null
          }
          <Button>Registrarse</Button>
        </form>
      </Card>
    </div>
  )
}

export default RegisterPage